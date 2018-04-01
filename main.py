import re



def fun (word):
    spisok = re.findall(r'\w+', word)
    my_dict = dict((i,spisok.count(i))for x,i in enumerate(spisok))
    return(dict(sorted(my_dict.items(), reverse = True)))

word = "трижды трижды трижды четырежды четырежды четырежды четырежды дважды дважды"
