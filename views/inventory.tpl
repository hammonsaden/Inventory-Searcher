% rebase('views/layout.tpl', title='inventory')


<body>
    <h1> Inventory </h1>
    <p>
    <table class='table'>
    <tr><th>Item Name</th><th>Quantity In Stock</th><th>Price Each</th></tr>
    %for row in rows:
        % for col in row:
            <td>{{col}}</td>
        %end
        </tr>
    </p>
%end
</table>
</body>