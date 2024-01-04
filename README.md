<img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=Rnaveennithyakalyan.nnkurlparser" />
<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&duration=4000&lines=nnkurlparser;" />
</h1>


## Overview
The urlparser script takes a list of URLs as input,parses them and generates a list of unique endpoint URLs by removing path components from each original URL.
This is the tool which is used as a Bugbounty automation tool for splitting endpoints from recon data.
It is used to parser the url according to our desire so we can have a detailed and proper implementation of our attacks for Bugbounty.

## Prerequisites
<div align="left">
    <a href="https://skillicons.dev">
        <img src="https://skillicons.dev/icons?i=python" />
    </a>
</div>    
Python installed on our system

## Installation
The Installation can be proceeded further by the following command in the terminal:
1.Install pip package:

````
pip install nnkurlparser
````
## Using in programs
````
from nnkurlparser import read_urls, main

input_filename = "input.txt"
output_filename = "output.txt"

urls = read_urls(input_filename, output_filename)
print("Parsed URLs:", urls)

# You can also call the main function if needed
# main()
#Remember to replace "input.txt" and "output.txt" with the actual file names you want to use.

````

## Tool Description
This tools is used to automate the url parser procedure and as a result of which we prioritize and execute the bug bounty process and look for the bugs in a more systematic way!

## Contact Me:
<div align="center"> 
  <a href="mailto:naveennithyakalyan@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red"/>
  </a>
  <a href="https://www.linkedin.com/in/r-naveen-nithya-kalyan-5474bb1b7">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</div>



 