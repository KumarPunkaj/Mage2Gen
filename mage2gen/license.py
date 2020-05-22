# A Magento 2 module generator library
# Copyright (C) 2016 Maikel Martens
#
# This file is part of Mage2Gen.
#
# Mage2Gen is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import os, datetime
from .utils import DefaultFormatter

LICENCE_DIR = os.path.join(os.path.dirname(__file__), 'licenses')

class License:
	identifier = 'proprietary'

	def __init__(self, copyright='', module_name='', description='', license_text='', short_license_text=''):
		self.license_text = license_text
		self.short_license_text = short_license_text
		self.copyright = copyright
		self.module_name = module_name
		self.description = description
		self.license_year = datetime.datetime.now().year
	
	def get_text(self):
		formatter = DefaultFormatter()
		return formatter.format(
			self.license_text,
			copyright=self.copyright,
			module_name=self.module_name,
			description=self.description,
			license_year=self.license_year
		)
	
	def get_short_text(self):
		formatter = DefaultFormatter()
		return formatter.format(
			self.short_license_text,
			copyright=self.copyright,
			module_name=self.module_name,
			description=self.description,
			license_year=self.license_year
		)
	
	def get_php_docstring(self):
		return '/**\n * Copyright © {copy_right} All rights reserved.\n * See COPYING.txt for license details.\n */\n'\
			.format(copy_right=self.copyright)


class FileLicense(License):
	template_license = None
	template_short_license = None

	def __init__(self, copyright='', module_name='', description='', *args, **kwargs):
		with open(os.path.join(LICENCE_DIR, self.template_license), 'rb') as tmpl:
			license_text = tmpl.read().decode('utf-8').strip()
			
		with open(os.path.join(LICENCE_DIR, self.template_short_license), 'rb') as tmpl:
			short_license_text = tmpl.read().decode('utf-8').strip()

		super().__init__(copyright, module_name, description, license_text, short_license_text)



class GPLV3(FileLicense):
	template_license = 'gplv3.txt'
	template_short_license = 'gplv3_short.txt'
	identifier = 'GPL-3.0'


class OSLV3(FileLicense):
	template_license = 'oslv3.txt'
	template_short_license = 'oslv3_short.txt'
	identifier = 'OSL-3.0'

class MIT(FileLicense):
	template_license = 'mit.txt'
	template_short_license = 'mit.txt'
	identifier = 'MIT'

class APACHE2(FileLicense):
	template_license = 'apache2.txt'
	template_short_license = 'apache2_short.txt'
	identifier = 'Apache-2.0'