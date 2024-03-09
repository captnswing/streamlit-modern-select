import {
    Streamlit,
    StreamlitComponentBase,
    withStreamlitConnection,
} from "streamlit-component-lib"
import React, {ReactNode} from "react"

interface State {
    selectedOption: string
    isFocused: boolean
}

class ModernSelect extends StreamlitComponentBase<State> {
    public state = {selectedOption: '', isFocused: false}

    public render = (): ReactNode => {
        // Arguments that are passed to the plugin in Python are accessible
        // via `this.props.args`.
        const options = this.props.args["options"]
        const size = this.props.args["size"]
        return (
            <span>
        Hello!<br/>
        <select
            size={size}
            onChange={this.onSelectionChange}
        >
            {options.map((option: string) => (
                <option key={option} value={option}>
                    {option}
                </option>
            ))}
        </select>
      </span>
        )
    }

    private onSelectionChange = (event: React.ChangeEvent<HTMLSelectElement>): void => {
        const selectedOption = event.currentTarget.value;
        this.setState(
            {selectedOption: selectedOption},
            () => Streamlit.setComponentValue(this.state.selectedOption)
        )
    }

    private _onFocus = (): void => {
        this.setState({isFocused: true})
    }

    private _onBlur = (): void => {
        this.setState({isFocused: false})
    }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(ModernSelect)
