# print(pow(101, 17, 22663))
# print(pow(base, exp, modulus))

# print(pow(12, 65537, 391))
# print(pow(12, 65537, 882564595536224140639625987659416029426239230804614613279163))
# euler's totient function
# for p and q prime, ϕ(n) = (p-1)(q-1)
p = 857504083339712752489993810777
q=1029224947942998075080348647219
# x= (p-1)*(q-1)
y= p*q
# #the flag was in X
# print(x,y)

#d is the modular multiplicative inverse of e mod ϕ(n)
# i.e., d ≡ e^(-1) (mod ϕ(n))
# e*d ≡ 1 (mod ϕ(n))
e=65537
phi_n = (p-1)*(q-1)
d = pow(e, -1, phi_n)
print(d)