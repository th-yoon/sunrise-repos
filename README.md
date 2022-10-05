# SunriseRepos: Unarchive batches of GitHub repositories

## Installation

Create a GitHub personal access token. The application will prompt you
for the value of your token each time you run it.

The application is available at PyPI. Install it from there using the following
command:

```
pip install sunrise-repos
```
----

You can also install directly from the source code by issuing the following
command in the project root:

```
pip install .
```
----


## Usage

Create a text file containing a batch of repositories listed in a
single column, then point the program to the file, using the following
command template:

```
sunrise-repos <GitHub organisation> <CSV file>
```
----

An example using process substitution to handle a single repository:

```
sunrise-repos GITHUB_ORGANISATION <(echo REPOSITORY_NAME)
```
----

## Trouble shooting
If it does not work as expected,  
1. Try hard-coding your personal token (only on your own machine) or changing your command console.  
2. Try changing the encoding of the csv file to ANSI.
----

### Reference
* https://www.lotharschulz.info/2020/11/02/repository-archiving-unarchiving-with-github-graphql-api/
* https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
* https://github.com/deriksson/sunset-repos
