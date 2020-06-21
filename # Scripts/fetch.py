# -*- coding: utf-8 -*-

#fetch Gravatars
# https://code.google.com/p/gource/wiki/GravatarExample

import os
import requests
import subprocess
import hashlib
import re 
from PIL import Image
from colorama import init, Fore, Back, Style

init(autoreset=True)

def md5_hex(text):
	m = hashlib.md5()
	m.update(text.encode('ascii', errors='ignore'))
	return m.hexdigest()

size = 256
output_dir = os.path.join('..', '..', 'Avatar')
temp_dir = os.path.join('..', '..', 'Temp')

os.makedirs(output_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

gitlog = subprocess.check_output(['git', 'log', '--pretty=format:%ae|%an'])
authors = set(gitlog.decode('ascii', errors='ignore').splitlines())

print(authors)
print('\n' + Style.BRIGHT + 'Downloading avatars...\n')

for author in authors:
	try:
		email, name = author.split('|')
		output_file = os.path.join(output_dir, name + '.png')
		temp_file = os.path.join(temp_dir, name + '.png')
		if email.endswith('@users.noreply.github.com'):
			name = re.findall("\d+\+(\w+)@users\.noreply\.github\.com", email)[0]
		if name.endswith('[bot]'):
			name = name[:-5]

		if not os.path.exists(output_file) and not os.path.exists(temp_file) :

			# Fetches from GitHub first

			gh_url = "https://avatars.githubusercontent.com/" + name + "?size=" + str(size)
			print(Style.BRIGHT + "Trying " + name + " (" + email + ") using GitHub...")
			r = requests.get(gh_url)

			# Check for dimensions. If w = 420, not found.

			with open(temp_file, 'wb') as img:
				img.write(r.content)
			im = Image.open(temp_file)

			if im.width != 420:
				print(Style.BRIGHT + Fore.WHITE + Back.GREEN + "Success!")
				with open(output_file, 'wb') as img:
					img.write(r.content)
			else:
				print(Style.BRIGHT + Fore.WHITE + Back.RED + "No avatar found on GitHub!")
				grav_url = "http://www.gravatar.com/avatar/" + md5_hex(email) + "?d=404&s=" + str(size)
				print(Style.BRIGHT + "Trying " + name + " (" + email + ") using Gravatar...")
				r = requests.get(grav_url)
				if r.status_code != 404:
					print(Style.BRIGHT + Fore.WHITE + Back.GREEN + "Success!")
					with open(output_file, 'wb') as img:
						img.write(r.content)
				else: 
					print(Style.BRIGHT + Fore.WHITE + Back.RED + "No avatar found on Gravatar!")
	except:
		print(Style.BRIGHT + Fore.WHITE + Back.RED + "Whoops, something went wrong. Try again later.")
					
print('\n' + Style.BRIGHT + 'All done!\n')
