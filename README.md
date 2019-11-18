# Add support for [norEduPerson](https://docs.feide.no/schema/noredu/index.html) tag in XML CAS response

[![Django](https://img.shields.io/badge/Django-2.2.3-green.svg)](https://www.djangoproject.com/weblog/2019/jul/01/security-releases/)
[![Python 3.7.3](https://img.shields.io/badge/python-3.7.3-green.svg)](https://www.python.org/)
[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=P3DGL6EANDY96&source=url)
[![License BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Follow JV conseil – Internet Consulting on Twitter](https://img.shields.io/twitter/follow/JVconseil.svg?style=social&logo=twitter)](https://twitter.com/JVconseil)

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

# Sponsorship

If this project helps you reduce time to develop, you can give me a cup of coffee ☕️ :-)

[![Donate with PayPal](https://www.paypalobjects.com/en_US/FR/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=P3DGL6EANDY96&source=url)