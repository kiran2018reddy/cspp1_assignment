"""code"""
def paying_debt(balance_1, annual_interest_rate):
    """code"""
    mfmp_ = 0
    temp_bal = balance_1
    year_count = 1
    while balance_1 > 0:
        mfmp_ += 10
        balance_1 = temp_bal
        i = 0
        # print(mfmp_,year_count)
        for i in range(1, 13):
            m_intrest_rate = annual_interest_rate/12.0
            monthly_unpaid_balance = balance_1 - mfmp_
            balance_1 = monthly_unpaid_balance + m_intrest_rate*monthly_unpaid_balance
            i = i+1
            # balance_1 = updated_balance_each_month
            # print (i,balance_1)
        # if balance_1 <=0.5:
        #     break
        year_count += 1
    return mfmp_
def main():
    """code"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debt(data[0], data[1]))
if __name__ == "__main__":
    main()