import json
import git


def get_commit_info(repo_path, file_path=None):

    repo = git.Repo(repo_path)

    commits_info = []

    for commit in repo.iter_commits(paths=file_path):
        commit_info = {
            "commit": commit.hexsha,
            "author": f"{commit.author.name} <{commit.author.email}>",
            "date": commit.authored_datetime.isoformat(),
            "message": commit.message.strip(),
            "changes": []
        }

        if len(commit.parents) > 0:
            parent = commit.parents[0]
        else:
            parent = commit.parents
            # Get code changes for each commit
        for diff in commit.diff(parent, create_patch=True):
            commit_info["changes"].append({
                "filename": diff.a_path,
                "additions": diff.diff.decode('utf-8', 'ignore').count('+'),
                "deletions": diff.diff.decode('utf-8', 'ignore').count('-'),
                "diff": diff.diff.decode('utf-8', 'ignore'),
                "new_file": diff.a_blob.data_stream.read().decode('utf-8', 'ignore') if diff.a_blob else '',
                "old_file": diff.b_blob.data_stream.read().decode('utf-8', 'ignore') if diff.b_blob else '',
            })

        commits_info.append(commit_info)

    return commits_info


def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    for (n, t, h) in \
        (('repo_path', str, 'path to the repository'),
         ('output_path', str, 'output file path')):
        parser.add_argument(n, type=t, help=h, required=True)
    args = parser.parse_args()
    save_to_json(
        get_commit_info(args.repo_path),
        args.output_path
    )

    




