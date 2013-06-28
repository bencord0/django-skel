======
README
======

Usage
=====

Install
=======

While not strictly required, it is also recommended to do

     $ SECRET_KEY=$(python -c 'import random;
         print "".join([random.choice(
               "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
         ) for i in range(50)])')
     $ heroku config:add SECRET_KEY=$SECRET_KEY

The production settings pull SECRET_KEY from environment but fallbacks
to a value which is generated mainly for development environment.

This setup allows you to easily keep your site in a public repo if you so 
wish without causing opening a route to attack your Django passwords.
