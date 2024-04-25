% rebase('views/layout.tpl', title='SubmitOrder')


<body>
    <h1> Order Item </h1>
    <form action="/SubmitOrder" method='post'>
        <label for='item_name'>Select Item to Order:</label>
        <select id="item_name" name="item_name">
            <option value="Banana">Banana</option>
            <option value="Apple">Apple</option>
            <option value="Milk">Milk</option>
            <option value="Eggs">Eggs</option>
        </select>
        <br>
        <label for="ordered">Enter Quantity to Order</label>
        <input type="number" id="ordered" name="ordered" min="1" required>
        <br>
        <input type="submit" value="Submit Order">
    </form>
    <br>
    <p>
    You Will Get Redirected to the Order Viewer if Order is successful.
    </p>
</body>
