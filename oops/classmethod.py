class demo:
    ins="hello"
    @classmethod
    def greet(cls):
        print("Hello")

    @classmethod 
    def modify(cls,new_value):
        cls.ins=new_value
        

demo.greet()
print(demo.ins)
demo.modify("swanandi")
print(demo.ins)



