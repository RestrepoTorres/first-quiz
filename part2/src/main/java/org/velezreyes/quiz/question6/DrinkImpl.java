package org.velezreyes.quiz.question6;

public enum DrinkImpl implements Drink{

    KarenTea("KarenTea",false, 1f),
    ScottCola("ScottCola", true, 0.75f);
    private final String name;
    private final boolean isFizzy;
    private final float price;
    DrinkImpl(String name, boolean isFizzy, float price)  {
        this.name = name;
        this.isFizzy = isFizzy;
        this.price = price;
    }
    public float getPrice(){
        return price;
    }
    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return isFizzy;
    }

    public static DrinkImpl getDrink(String name) throws UnknownDrinkException {
        for (DrinkImpl drink : values()) {
            if (drink.name().equalsIgnoreCase(name)) {
                return drink;
            }
        }
        throw new UnknownDrinkException();
    }
}




