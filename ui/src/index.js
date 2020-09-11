// debug
import {Model} from "./Model";
import {initializeSocket} from "./socket";
import {initializeDebugElements} from "./debug";
import {Display} from "./Display";

initializeDebugElements();

// Apply gameevent to the model
let model = new Model();

initializeSocket(event => model.doEvent(event));

