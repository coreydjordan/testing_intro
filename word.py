class TextInfo():  
    def count_vowels(self, text):
        v_count = 0
        c_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in text:
            if i in vowels:
                v_count += 1
            else:
                c_count += 1
        return v_count       
    def count_cons(self, text):
        v_count = 0
        c_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in text:
            if i in vowels:
                v_count += 1
            else:
                c_count += 1
        return c_count       

        
        
        
        
if __name__ == '__main__':
    wrd = TextInfo()
    print(wrd.count_vowels('hello world'))
    print(wrd.count_cons('hello world'))
    
        