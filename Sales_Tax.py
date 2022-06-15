def get_detail_of_product(n):
        n1=n.split()
        price=n1[-1].strip()
        st=n[0:len(n)-len(price)-4].strip()
        price=float(price)
        qua=st.split()[0]
        lent=len(qua)
        qua=int(qua)
        item=st[lent:].strip()
        return [qua,item,price,st]

def exempted_cal(n):
    total_cost=0
    k=n
    exempted=["books","chocolates","pills","book","chocolate","pill"]
    n1=n.split()
    for i in n1:
        if i.lower() in exempted:
            return True
        

def calc_tax_exempted(n):
    k=n
    n1=n.split()
    qua,it,pr,st=get_detail_of_product(k)
    imp=["imported","import"]
    for i in n1:
        if i in imp:
            cst_sls_tx=(pr*qua)+(0.05*pr)
            break

        else:
            cst_sls_tx=(pr*qua)

    return round(cst_sls_tx,2)

def calc_tax(n):
    k=n
    n1=n.split()
    imp=["imported","import"]
    qua,it,pr,st=get_detail_of_product(k)
    for i in n1:
        if i in imp:
            cst_sls_tx=(pr*qua)+(0.1*pr)+(0.05*pr)
            break
                
        else:
            cst_sls_tx=(pr*qua)+(0.1*pr)
            
            
        
    return round(cst_sls_tx,2)
def printing_products(n):
    k=n
    c=exempted_cal(k)
    d=calc_tax_exempted(k)
    e=calc_tax(k)
    qua,it,pr,st=get_detail_of_product(k)
    if c==True:
        return str(qua)+ " "+str(it)+":"+str(d)
    else:
        return str(qua)+ " "+str(it)+":"+str(e)

            
        
new_p=[]
m=[]
s=[]
org_price=[]
inputs=int(input("Please enter how many products that has to be  billed: "))
for i in range(0,inputs):
    product=input()
    qua,item,price,st=get_detail_of_product(product)
    org_price.append(round(price,2))
    aa=exempted_cal(product)
    print(aa)
    if aa==True:
        new_p.append(round(calc_tax_exempted(product),2))
    else:
        new_p.append(round(calc_tax(product),2))
    s.append(printing_products(product))



for i in s:
    print(i)

sum_n=sum(new_p)
sales_tax=sum(new_p)-sum(org_price)

print("sales tax is :"+ str(round(sales_tax,2)))
print("total :" ,sum_n)















