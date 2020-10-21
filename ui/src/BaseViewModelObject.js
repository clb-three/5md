export class BaseViewModelObject {
    constructor(viewModel) {
        this.vm = viewModel;
        this.view = viewModel.view;
    }
}