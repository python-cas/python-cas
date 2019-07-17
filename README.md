[![Django](https://img.shields.io/badge/Django-2.2.3-green.svg)](https://www.djangoproject.com/weblog/2019/jul/01/security-releases/)
[![Python 3.7.3](https://img.shields.io/badge/python-3.7.3-green.svg)](https://www.python.org/)
[![License BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Follow JV conseil – Internet Consulting on Twitter](https://img.shields.io/twitter/follow/JVconseil.svg?style=social&logo=twitter)](https://twitter.com/JVconseil)


# Add support for [norEduPerson](https://docs.feide.no/schema/noredu/index.html) tag in XML CAS response
To allow attributes to be retrieved from `<norEduPerson>` nested elements when there is no `<cas:attributes>` available in the XML CAS response file:
```
<cas:serviceResponse xmlns:cas="http://www.yale.edu/tp/cas">
    <cas:authenticationSuccess>
        <cas:user>UserName</cas:user>
        <norEduPerson>
            <mail>UserEmail</mail>
            <sn>UserLastName</sn>
            <gn>UserFirstName</gn>
        </norEduPerson>
    </cas:authenticationSuccess>
</cas:serviceResponse>
```