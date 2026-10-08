import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch


class ScraperTests(unittest.TestCase):
    def setUp(self):
        path = Path(__file__).resolve().parents[1] / 'Indeed_job.py'
        spec = importlib.util.spec_from_file_location('indeed_test_scraper', path)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def test_distinct_job_ids_produce_distinct_urls(self):
        response = Mock()
        response.text = '''<ul class="css-zu9cdh">
        <div class="job_seen_beacon"><h2 class="jobTitle"><a data-jk="first">First</a></h2></div>
        <div class="job_seen_beacon"><h2 class="jobTitle"><a data-jk="second">Second</a></h2></div>
        </ul>'''
        scraper = Mock()
        scraper.get.return_value = response
        with patch.object(self.module.cloudscraper, 'create_scraper', return_value=scraper), patch.object(self.module, 'export') as export:
            self.module.scrape_job()
        jobs = export.call_args.args[0]
        self.assertEqual([job['job url'] for job in jobs], [
            'https://pk.indeed.com/viewjob?jk=first',
            'https://pk.indeed.com/viewjob?jk=second',
        ])

    def test_repeated_export_does_not_duplicate_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'jobs.csv'
            with patch.object(self.module, 'Path', return_value=target):
                self.module.export([{'title': 'First'}])
                self.module.export([{'title': 'Second'}])
            self.assertEqual(target.read_text().splitlines(), ['title', 'First', 'Second'])

if __name__ == '__main__':
    unittest.main()
