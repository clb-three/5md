import * as loglevel from "loglevel";
import {BaseViewModelObject} from "./BaseViewModelObject";

const log = loglevel.getLogger("display::Target");

export class Target extends BaseViewModelObject {
    constructor(vm) {
        super(vm);

        const x = 300;
        const y = 300;
        log.debug("(x, y)", x, y);

        this.sprite = this.vm.view.sprite(`images/badguy.png`, x, y, 100, 160);
        this.type = this.vm.view.text("", x, y);
        this.symbols = this.vm.view.text("", x, y + 50);
    }

    containsPoint(point) {
        log.info("testing if point", point, "is in the target display");
        const result = this.sprite.containsPoint(point);
        log.info("point", point, "in the target display:", result);
        return result;
    }

    drawEnemy(enemy) {
        log.debug('draw enemy', enemy);

        this.sprite.texture = this.view.texture(`images/badguy.png`);
        this.type.text = enemy.type;
        this.setSymbols(enemy.symbols);
    }

    setSymbols(symbols) {
        log.debug('set enemy symbols', symbols);

        this.symbols.text = symbols;
    }
}