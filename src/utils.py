
def load_args():
    from dotenv import load_dotenv
    load_dotenv()
    return {
        'api_key': os.environ.get("OPENAI_API_KEY"),
        'repo_path': os.environ.get("REPO_PATH"),
    }

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    for (n, t, h) in \
        (('api_key', str, 'openai api key'),
         ('repo_path', str, 'path to the repository')):
        parser.add_argument(n, type=t, help=h, required=True)
    return parser.parse_args()

