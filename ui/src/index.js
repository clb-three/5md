import * as log from "loglevel";
import {initializeSocket} from "./socket";
import {initializeDebugElements} from "./debug";
import {Display} from "./Display";

log.setDefaultLevel('debug');

initializeDebugElements();

const display = new Display();
initializeSocket(e => display.doEvent(e));

