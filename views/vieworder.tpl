% rebase('views/layout.tpl', title='order viewer')


<body>
    <h1> Orders </h1>
    <p>
    <table class='table'>
    <tr><th>Date Ordered</th><th>Item Name</th><th>Ordered</th><th>Price Each</th><th>Total</th></tr>
    %for row in rows:
        % for col in row:
            <td>{{col}}</td>
        %end
        </tr>
    </p>
%end
</table>
</body>