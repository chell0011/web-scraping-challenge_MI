#!/usr/bin/env python
# coding: utf-8


#Import dependencies 
from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape():

	#Path to chromedriver
	executable_path = {'executable_path':'C:\\Users\\Chell\\Documents\\Training\\GWU\\Wk12- Web Scraping\\chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)


	#NASA Mars News
	url = 'https://mars.nasa.gov/news/'
	browser.visit(url)

	#HTML object
	#Parse HTML with Beautiful Soup
	html_news = browser.html
	soup_news = BeautifulSoup(html_news, 'html.parser')

	#Scrape news title and paragraph text 
	news_title = (soup_news.find('div', class_='content_title')).string
	news_para = (soup_news.find('div', class_='article_teaser_body')).string



	#JPL Mars Space Images - Featured Image
	url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url2)

	#Base url variable
	baseurl = 'https://www.jpl.nasa.gov'

	#HTML object
	#Parse HTML with Beautiful Soup
	html2 = browser.html
	soup2 = BeautifulSoup(html2, 'html.parser')

	#Button to navigate page to full image
	button = soup2.find('a', class_='button fancybox')
	button

	#Find img url within page 
	image_url = soup2.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')

	#Featured image url 
	featured_image_url = baseurl + image_url



	#Mars Weather twitter account
	url3 = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url3)

	#HTML object
	#Parse HTML with Beautiful Soup
	html3 = browser.html
	soup3 = BeautifulSoup(html3, 'html.parser')

	#Find tweet 
	tweet = soup3.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

	#Scrape tweet
	mars_weather = tweet.text.strip()



	#Mars Facts
	url4 = 'https://space-facts.com/mars/'
	tables = pd.read_html(url4)
	#Create df
	df = tables[0]
	#DF to HTML
	print(df.to_html())



	#Mars Hemispheres 
	url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url5)

	#HTML object
	#Parse HTML with Beautiful Soup
	html5 = browser.html
	soup5 = BeautifulSoup(html5, 'html.parser')

	# Retreive all items that contain mars hemispheres information
	items = soup5.find_all('div', class_='item')

	# Create empty list for hemisphere urls 
	hemisphere_image_urls = []

	# Store the base_ul 
	hemispheres_base_url = 'https://astrogeology.usgs.gov'

	# Loop through the items previously stored
	for i in items: 
		# Store title
		title = i.find('h3').text
		
		# Store link that leads to full image website
		partial_img_url = i.find('a', class_='itemLink product-item')['href']
		
		# Visit the link that contains the full image website 
		browser.visit(hemispheres_base_url + partial_img_url)
		
		# HTML Object of individual hemisphere information website 
		partial_img_html = browser.html
		
		# Parse HTML with Beautiful Soup for every individual hemisphere information website 
		soup6 = BeautifulSoup( partial_img_html, 'html.parser')
		
		# Retrieve full image source 
		img_url = hemispheres_base_url + soup6.find('img', class_='wide-image')['src']
		
		# Append the retreived information into a list of dictionaries 
		hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
		

	mars_data = {
     "News_Title": news_title,
     "Paragraph_Text": news_para,
     "Most_Recent_Mars_Image": featured_image_url,
     "Mars_Weather": mars_weather,
     "Mars_Hem": hemisphere_image_urls
     }


	return mars_data








