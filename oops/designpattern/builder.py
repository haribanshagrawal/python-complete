# words=['hello','World']
# parts=['<ul>']
# for w in words:
#     parts.append(f' <li>{w}<li>')
# parts.append('<ul>')
# print('\n'.join(parts))
    
class HtmlElement:
    indent_size=2
    
    def __init__(self,name='',text=''):
        self.text=text
        self.name=name
        self.elements=[]    
    
    def __str(self,indent):
        #print('printing 1')
        lines=[]
        i=' '*(indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')
        
        if self.text:
            i1=' ' * ((indent +1) * self.indent_size)
            lines.append(f'{i1}{self.text}')
            
        for e in self.elements:
            lines.append(e.__str(indent +1))
        
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
        
    def __str__(self):
        return self.__str(0)
    
    
class HtmlBuilder:
    def __init__(self,root_name):
        self.root_name=root_name
        self.__root=HtmlElement(root_name)
        #print(self.__root)
    
    def add_child(self,child_name,child_text):
        self.__root.elements.append(
            HtmlElement(child_name,child_text))    
        
    def __str__(self):
        #print('printing')
        return str(self.__root)
    
builder=HtmlBuilder('ul')
builder.add_child('li','hello')
builder.add_child('li','world')
print('Ordinary Builder')
print(builder)