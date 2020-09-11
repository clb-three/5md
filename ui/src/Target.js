export class Target {
    constructor(display) {
        this.display = display;
        const x = 300;
        const y = 300;

        const target = this.display.sprite(`images/badguy.png`, x, y, 100, 160);
        const targetType = this.display.text("", x, y);
        const targetSymbols = this.display.text("", x, y + 50);

        this.targetDisplay = {
            target,
            targetType,
            targetSymbols
        };
    }

    setTarget(enemy) {
        this.targetDisplay.target.texture = this.display.texture(`images/badguy.png`);
        this.targetDisplay.targetType.text = enemy.type;
        this.setSymbols(enemy.symbols);
    }

    setSymbols(symbols) {
        this.targetDisplay.targetSymbols.text = symbols;
    }
}