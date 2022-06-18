import React, { Component } from "react";
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      sum: 0,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/order/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            sum: data.map(order => {
              return (order.dollar_value)
            }).reduce(function (sum, elem) {
              return sum + elem;
            }),
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <div className="orders">
        <div className="total">
          <span className="total__text">Total</span>
          <span className="total__number">{this.state.sum}</span>
        </div>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={this.state.data.map(order => {
            return ({ name: order.delivery_time, uv: order.dollar_value })
          })} margin={{ top: 5, right: 20, bottom: 5, left: 30 }}>
            <Line type="monotone" dataKey="uv" stroke="#8884d8" />
            <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
          </LineChart>
        </ResponsiveContainer>
        <div className="name-grid">
          <div className="order__item">
            №
          </div>
          <div className="order__item">
            заказ №
          </div>
          <div className="order__item">
            стоимость, $
          </div>
          <div className="order__item">
            срок поставки
          </div>
        </div>
        {this.state.data.map(order => {
          return (
            <div className="order" key={order.order_number}>
              <div className="order__item">
                {order.index}
              </div>
              <div className="order__item">
                {order.order_number}
              </div>
              <div className="order__item">
                {order.dollar_value}
              </div>
              <div className="order__item">
                {order.delivery_time}
              </div>
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;