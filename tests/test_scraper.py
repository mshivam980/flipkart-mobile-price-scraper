import os
from scraper.scrape_flipkart import scrape_flipkart_data

def test_scraper():
    output_file = "output/test_output.csv"
    scrape_flipkart_data(pages=1, output_file=output_file)
    assert os.path.exists(output_file), "Output CSV not generated!"
