*********************
How To Make A Release
*********************

1. Update `docs/changelog.txt`
2. Update version in `docs/conf.py`, `setup.py`.
3. commit changes.
4. Tag a version, e.g.

    git tag v1.0.0

5. push changes:

    git push
    git push --tags

6. Upload release to pypi.python.org

    python setup.py sdist bdist_wheel upload

7. Create a new release on https://github.com/python-cas/python-cas/releases
