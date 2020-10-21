import {ViewModel} from "./ViewModel";
import {View} from "./View";

export class BaseViewModelObject {
    vm: ViewModel;
    view: View;

    constructor(viewModel) {
        this.vm = viewModel;
        this.view = viewModel.view;
    }
}