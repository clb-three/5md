import * as log from "loglevel";
import {initializeSocket} from "./socket";
import {initializeDebugElements} from "./debug";
import {ViewModel} from "./ViewModel";

log.setDefaultLevel('debug');

initializeDebugElements();

const display = new ViewModel();
initializeSocket(e => display.doEvent(e));

