from typing import Dict, Text
from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def ingrese():
    string_arg = request.args.get("text", "")
    result=manipulate(string_arg)
    return render_template("ingrese.html", result=result)

def manipulate(text: str):
    result = {}
    if text== "":
        return result
    result["string"] = text
    result["reverse"] = text[::-1]
    result["len"] = len(text)
    result["vowels"] = vowel_count(text)
    result["consonants"] = consonant_count(text)
    result["upper"] = text.upper()
    result["lower"] = text.lower()
    result["updown"] = updown(text)
    result["naive"] = naive(text)

    return result
    
def vowel_count(text: str, vowel=True):
    num_vowels=0
    for char in text:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

def consonant_count(text: str, vowel=False):
    con_vowels=0
    for char in text:
        if char not in "aeiouAEIOU":
           con_vowels = con_vowels+1
    return con_vowels

def updown(text: str):
  texto = ""
  letters = 1
  for char in text:
    if letters == 1:
      texto += char.upper()
      letters = letters -1
    else:
      texto += char.lower()
      letters = letters + 1
  return texto

def naive(text: str):
    texto = ""
    texto = text.replace("a", "@").replace("e", "3").replace("i", "!").replace("o", "0").replace("u", ")")
    return texto
 


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)