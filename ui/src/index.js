import {Model} from "./Model";
import {initializeSocket} from "./socket";
import {initializeDebugElements} from "./debug";
import {Display} from "./Display";

initializeDebugElements();

const display = new Display();
let model = new Model(display);
initializeSocket(e => model.doEvent(e));

