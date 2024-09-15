# How to Release
This doc is to remind my future self how to release to PyPi.
## Versioning
Versions are automatically generated from the git history by [setuptools_scm](https://setuptools-scm.readthedocs.io/en/stable/). The most recent git tag is incremented, then a dev string is appended with the count of commits since that tag. The `local_scheme` part of the version (the commit's hash) is omitted because it is incompatible with PyPi. Also it's ugly.
```
$ python -m setuptools_scm
1.0.1.dev1
```
## Test Environment
All commits are built and pushed to the [test environment](https://test.pypi.org/project/etawatch/) automatically.
## Prod Environment
To release a new version to the [prod environment](https://pypi.org/project/etawatch/), a tag must be pushed _by itself_, because the CI/CD pipeline looks for if the push is a tag only. To do this, you first must push your final commits.
```
$ git commit -m "Release 1.0.0"
$ git push
```
Next, you need to grab the hash of the final release commit.
```
$ git log --pretty=oneline
49464d79bb9d75a309dfb0d453b042840e19c516 (HEAD -> main, origin/main, origin/HEAD) Release 1.0.0
...
...
...
```
Now create an annotated tag locally on that commit. Because `setuptools_scm` guesses the next version by incrementing the __patch__ version specifically, all tags must be the full [semver](https://semver.org/) syntax.
```
$ git tag -a 1.0.0 49464d79bb9d75a309dfb0d453b042840e19c516
```
Finally, push the tag to remote to trigger the prod CI/CD build.
```
$ git push origin tag 1.0.0
```