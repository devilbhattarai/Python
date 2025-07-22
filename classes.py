class computer:
    def __init__(self,cpu,ram,gpu):
        self.cpu=cpu
        self.ram=ram
        self.gpu=gpu
        print(f"You got {cpu} along with {ram} RAM and a {gpu} graphics card")

    def specs(com2,cpu):
        print(cpu)

com1=computer("i5-13300HS","128 GB","NVIDIA RTX 5090")
com2=computer("i5-13S","12 GB","NV 5090")