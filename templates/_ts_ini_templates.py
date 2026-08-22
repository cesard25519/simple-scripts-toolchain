counter_model: str = """import { state } from "lit/decorators.js";
import { LitElement } from "lit";


export class Counter extends LitElement {
    @state() value = 0;

    __increment(): void { this.value++; }
    __reset(): void { this.value = 0; }
    __decrement(): void { this.value--; }
}
"""


counter_component: str = """import { html, unsafeCSS, type HTMLTemplateResult } from "lit";
import { customElement } from "lit/decorators.js";
import { Counter } from "../models/counter";


import styled from '../styles/counter.css?inline';


@customElement('x-counter')
export class XCounter extends Counter {
    static styles = unsafeCSS(styled);

    protected render(): HTMLTemplateResult {
        return html`
            <h1>${ this.value }</h1>
            <button @click=${ this.__decrement }> - </button>
            <button @click=${ this.__reset }> RESET </button>
            <button @click=${ this.__increment }> + </button>
        `;
    }
}
"""

counter_style: str = """:host {
    --black: #091413;
    --green: #285a48;
    --green1: #408a71;
    --green2: #b0e4cc;
}

:host {
    background-color: var(--green);
    border-radius: 4px;
    padding: 5px 10px;
    display: block;
    margin: 0;
}

h1 {
    flex-direction: column;
    color: var(--green2);
    align-items: center;
    display: flex;
    margin: 10px;
}

button {
    background-color: var(--green1);
    border-color: transparent;
    color: var(--green2);
    border-radius: 4px;
    padding: 5px 10px;
}
"""
