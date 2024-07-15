from bing_image_downloader import downloader
import os

# Define search queries
search_queries = [
    "Virat Kohli",
    "Roger Federer",
    "Maria Sharapova",
    "Lionel Messi",
    "Serena Williams"
]

# Define the directory to save images
output_dir = 'imagedata'

# Create the directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download images
for query in search_queries:
    downloader.download(query, limit=10, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)
