
        using FreeSql.DataAnnotations;
        using System;

        public class Product {
            [Column(IsIdentity = true, IsPrimary = true)]
            public {DATA_TYPE} create_time { get; set; }
public {DATA_TYPE} id { get; set; }
public {DATA_TYPE} name { get; set; }
public {DATA_TYPE} product_code { get; set; }
public {DATA_TYPE} specification { get; set; }
        }