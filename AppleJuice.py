x_input=float(input("How many people are there?\n>"))
y_input=float(input("How many apples are there?\n>"))

def portion(y, x):
    return(y / x)

apple_portion=portion(y_input, x_input)

def serve(y_input, apple_portion):
    print("Serve " + "y_input"  + "glasses of apple juice at " + apple_portion + "apple per glass ")

portion(y_input, apple_portion)
serve(y_input, apple_portion)