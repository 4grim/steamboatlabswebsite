About:
=============

This is the template for a company website I built for Steamboat Labs in 2014 written in Django/Python. 

The website includes a few features that have been deliniated by separate apps:
+Projects App where clients and projects are recorded
+About section where each teammember is featured
+Company blog with markdown/pygments and dynamic image integration
+A contact form


Installation:
=============

One thing to note is the current setting file are set up with a Heroku/Postgres deployment using S3 as a media server so these pieces would need to be edited to reflect your development environment or create a local_settings.py file to accommodate both types of set up. Additionally, all the secret keys and passwords in the current files need to be changed to your accounts (the ones posted are no longer valid).

