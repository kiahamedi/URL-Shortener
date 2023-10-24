# URL-Shortener
URL Shortener is a tool to shorten a long link and create a short URL and QR-Code easy to share on sites, chat and emails. Track short URL traffic and manage your links.


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

# Demo
![Alt text](https://raw.githubusercontent.com/kiahamedi/URL-Shortener/main/Screenshot.png "Optional title")

# Login (OTP)
![Alt text](https://raw.githubusercontent.com/kiahamedi/URL-Shortener/main/ScreenshotLogin.png "Optional title")<br>
[Login Kiay.ir](https://kiay.ir/login/)

# Firefox Extention
![Alt text](https://raw.githubusercontent.com/kiahamedi/URL-Shortener/main/firefox_extention/Screenshot_firefox.png "Optional title")
[Install Firefox Extention](https://addons.mozilla.org/en-US/firefox/addon/kiay-shortener/)

# Install
```python
git clone https://github.com/kiahamedi/URL-Shortener.git
cd URL-Shortener/
pip install -r requirements.txt
cd app/
python manage.py migrate
```
<br>


# Run localhost
```python
python manage.py runserver
```
<br>

# Run TestCase
```python
python manage.py test shortner

Found 9 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.........
----------------------------------------------------------------------
Ran 9 tests in 0.022s

OK
Destroying test database for alias 'default'...
```
<br>


## Are you a developer?
> 1-Fork it!</br>
> 2-Create your feature branch: git checkout -b my-new-feature</br>
> 3-Commit your changes: git commit -am 'Add some feature'</br>
> 4-Push to the branch: git push origin my-new-feature</br>
> 5-Submit a pull request</br>
