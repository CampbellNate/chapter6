text = "X-DSPAM-Confidence:    0.8475"
pos= text.find(':')+1
string=text[pos:]
number=string.strip()
float(number)
print(number)
