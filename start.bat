title GreenOdoo - www.GreenOdoo.com
COLOR 0A
SET PATH="%CD%"\runtime\pgsql\bin;"%CD%"\runtime\python;%CD%\runtime\win32\wkhtmltopdf;%CD%\runtime\win32\nodejs;%PATH%.
"%CD%"\runtime\pgsql\bin\pg_ctl -D "%CD%"\runtime\pgsql\data -l "%CD%"\runtime\pgsql\logfile start
"%CD%"\runtime\python\python-oe "%CD%"\source\odoo-bin -c "%CD%"\openerp-server.conf
