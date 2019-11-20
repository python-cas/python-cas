# Add support for [norEduPerson](https://docs.feide.no/schema/noredu/noredu_ch02.html#relationship-to-other-ldap-schemas) tag in XML CAS response

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

## What is [norEduPerson](https://docs.feide.no/schema/noredu/noredu_ch02.html#relationship-to-other-ldap-schemas)?

> eduPerson is designed to support LDAP (Lightweight Directory Access Protocol) operations for campus directories designed to facilitate communication among higher education institutions. It consists of a set of data elements or attributes about individuals within higher education, along with recommendations on the syntax and semantics of the data that may be assigned to those attributes.
>
> The norEdu classes add further attributes supplementing eduPerson/eduOrg in order to satisfy the requirements of the environment of the Nordic educational community, such as support for National Identity Numbers (norEduPersonNIN) and for the educational numbering and identifier schemes.

Further reading:
- https://docs.feide.no/schema/noredu/noredu_ch02.html#relationship-to-other-ldap-schemas
- http://software.internet2.edu/eduperson/internet2-mace-dir-eduperson-201602.html#Introduction

## What is [CAS](https://yale.service-now.com/it?id=service_offering&sys_id=60684dcd6fbb31007ee2abcf9f3ee4fc)?

> CAS stands for Central Authentication Service. It provides NetID authentication and Single-Sign-On for web-based applications and protects thousands of websites at Yale:
> - When your application has been CASified, your users are presented with a single, consistent login page to enter their NetID and Password.
> - With the Single-Sign-On nature of CAS, individuals need only provide their NetID and Password once per browser session instead of for every site they navigate to.
> - Applications that implement the CAS protocol never see the individual's password, providing a safe and secure means to authenticate.
>
> CAS was developed by Yale University's Technology and Planning Group. As world-wide usage of the protocol expanded, support and maintenance of the system was turned over to JASIG (now Apereo).

Further reading:
- https://yale.service-now.com/it?id=service_offering&sys_id=60684dcd6fbb31007ee2abcf9f3ee4fc

# Sponsorship

If this project helps you reduce time to develop, you can give me a cup of coffee ☕️ :-)

[![Donate with PayPal](https://www.paypalobjects.com/en_US/FR/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=P3DGL6EANDY96&source=url)