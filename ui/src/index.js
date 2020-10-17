import * as log from "loglevel";
import {Model} from "./Model";
import {initializeSocket} from "./socket";
import {initializeDebugElements} from "./debug";
import {Display} from "./Display";

log.setDefaultLevel('debug');

initializeDebugElements();

const display = new Display();
let model = new Model(display);
initializeSocket(e => model.doEvent(e));

