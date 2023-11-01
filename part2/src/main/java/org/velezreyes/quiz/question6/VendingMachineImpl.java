package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
    private float money = 0;

    public static VendingMachine getInstance() {
        return new VendingMachineImpl();
    }

    @Override
    public void insertQuarter() {
        setMoney(getMoney() + 0.25f);
    }

    public float getMoney() {
        return money;
    }

    public void setMoney(float money) {
        this.money = money;
    }

    public void chargeMoney(float price) throws NotEnoughMoneyException {
        if (getMoney() - price < 0) {
            throw new NotEnoughMoneyException();
        }
        setMoney(getMoney() - price);
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        DrinkImpl selectedDrink = DrinkImpl.getDrink(name);
        this.chargeMoney(selectedDrink.getPrice());
        return selectedDrink;
    }
}
