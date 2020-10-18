def cmd():
    while True:
        if 2 == 2:
            for i in range(1, 10):
                print(i)
                break
        elif 1+1 == 2:
            for i in range(10, 1):
                print(i)
                break
                
canvas = Canvas(tk, width=300, height=300)
File = Button(tk, text="File", command=cmd)
Format = Button(tk, text="Format", command=cmd)
Edit = Button(tk, text="Edit", command=cmd)
File.grid(row=0, column=1)
Format.grid(row=0, column=2)
Edit.grid(row=0, column=3)
