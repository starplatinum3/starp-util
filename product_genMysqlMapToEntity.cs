
        using FreeSql.DataAnnotations;
        using System;

        public class Product {
            [Column(IsIdentity = true, IsPrimary = true)]
            
        DateTime create_time = DateTime.Now;
        DateTime.TryParse(reader["create_time"].ToString(), out create_time);
line.create_time = create_time;

        int id = 0;
        int.TryParse(reader["id"].ToString(), out id);
        line.id = id;
        
line.id = id;

        string name = reader["name"].ToString();
line.name = name;

        string product_code = reader["product_code"].ToString();
line.product_code = product_code;

        string specification = reader["specification"].ToString();
line.specification = specification;
        }