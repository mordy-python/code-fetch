import click
import requests

@click.command()
@click.argument('user')
@click.argument('repo')
@click.argument('file')
@click.option('--save', help='Save the file to disk', is_flag=True)
@click.option('--save-file', help='The output file')
def fetch_code(user, repo, file, save, save_file, **kwargs):
    '''Gets the code from a single file in a Github repository instead of cloning the whole thing'''
    url = f'https://raw.githubusercontent.com/{user}/{repo}/master/{file}'
    output = save_file if save_file else file
    if save:
        with open(output, 'w') as f:
            f.write(requests.get(url).text)
    else:
        print(requests.get(url).text)


if __name__ == '__main__':
    fetch_code()