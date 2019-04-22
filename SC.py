# -*- coding: utf-8 -*-

import sys
import rdflib

# Order1

g1 = rdflib.Graph()

# ... add some triples to g somehow ...

g1.parse("data.ttl", format = "n3")
g1.parse("outputfile1.ttl", format = "n3")

qres1 = g1.query(
    """PREFIX ns1: <http://example.org/>
       PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
       SELECT DISTINCT ?Product ?ItemIdentifier ?Price ?Quantity ?InStock ?ReadyForTransport ?ProductsToProduce ?ProductionTime ?NewProductsReadyIn
       WHERE {
          ?order ns1:ItemIdentifier ?ItemIdentifier.
          ?Product ns1:Identifier ?ItemIdentifier.
          ?order ns1:PriceAmount ?Price.
          ?order ns1:Quantity ?Quantity.
          ?Product ns1:AvailableInStock ?InStock.
          bind(if(xsd:integer(?InStock) >= xsd:integer(?Quantity),"True", "False") as ?ReadyForTransport).
          bind(if(xsd:integer(?InStock) >= xsd:integer(?Quantity),"0", xsd:integer(?Quantity) - xsd:integer(?InStock)) as ?ProductsToProduce).
          ?Product ns1:ProductionProcess ?Process.
          ?Process ns1:ProductionLine ?ProductionLine.
          ?ProductionLine ns1:ProductionTimePerItem ?TimePerItem.
          ?ProductionLine ns1:Machines ?Ms.
          ?Ms ns1:FreeIn ?MachineFreeIn.
          bind(if(xsd:integer(?ProductsToProduce) = 0, "",  xsd:integer(?TimePerItem) * xsd:integer(?ProductsToProduce)) as ?ProductionTime).
          bind(if(xsd:integer(?ProductsToProduce) = 0, "",  xsd:integer(?ProductionTime) + xsd:integer(?MachineFreeIn)) as ?NewProductsReadyIn).
          
       }
       ORDER BY DESC(xsd:integer(?MachineFreeIn)) LIMIT 1
       """)
       

print ('Product                  ItemIdentifier   Price   Quantity   AvailableInStock   ReadyForTransport  ProductsToProduce  ProductionTime    NewProductsReadyIn')
for row in qres1:
    print("%s  %s    %s    %s          %s               %s               %s                 %s                %s" % row)


# Order2

g2 = rdflib.Graph()

# ... add some triples to g somehow ...

g2.parse("data.ttl", format = "n3")
g2.parse("outputfile2.ttl", format = "n3")

qres2 = g2.query(
    """PREFIX ns1: <http://example.org/>
       PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
       SELECT DISTINCT ?Product ?ItemIdentifier ?Price ?Quantity ?InStock ?ReadyForTransport ?ProductsToProduce ?ProductionTime ?NewProductsReadyIn
       WHERE {
          ?order ns1:ItemIdentifier ?ItemIdentifier.
          ?Product ns1:Identifier ?ItemIdentifier.
          ?order ns1:PriceAmount ?Price.
          ?order ns1:Quantity ?Quantity.
          ?Product ns1:AvailableInStock ?InStock.
          bind(if(xsd:integer(?InStock) >= xsd:integer(?Quantity),"True", "False") as ?ReadyForTransport).
          bind(if(xsd:integer(?InStock) >= xsd:integer(?Quantity),"0", xsd:integer(?Quantity) - xsd:integer(?InStock)) as ?ProductsToProduce).
          ?Product ns1:ProductionProcess ?Process.
          ?Process ns1:ProductionLine ?ProductionLine.
          ?ProductionLine ns1:ProductionTimePerItem ?TimePerItem.
          ?ProductionLine ns1:Machines ?Ms.
          ?Ms ns1:FreeIn ?MachineFreeIn.
          bind(if(xsd:integer(?ProductsToProduce) = 0, "",  xsd:integer(?TimePerItem) * xsd:integer(?ProductsToProduce)) as ?ProductionTime).
          bind(if(xsd:integer(?ProductsToProduce) = 0, "",  xsd:integer(?ProductionTime) + xsd:integer(?MachineFreeIn)) as ?NewProductsReadyIn).
          
       }
       ORDER BY DESC(xsd:integer(?MachineFreeIn)) LIMIT 1
       """)
       
       
for row in qres2:
    print("%s  %s    %s    %s          %s                 %s               %s                 %s                %s" % row)


# Order3

g3 = rdflib.Graph()

# ... add some triples to g somehow ...

g3.parse("data.ttl", format = "n3")
g3.parse("outputfile3.ttl", format = "n3")

qres3 = g3.query(
    """PREFIX ns1: <http://example.org/>
       PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
       SELECT DISTINCT ?Product ?ItemIdentifier ?Price ?Quantity ?InStock ?ReadyForTransport ?ProductsToProduce ?ProductionTime ?NewProductsReadyIn
       WHERE {
          ?order ns1:ItemIdentifier ?ItemIdentifier.
          ?Product ns1:Identifier ?ItemIdentifier.
          ?order ns1:PriceAmount ?Price.
          ?order ns1:Quantity ?Quantity.
          ?Product ns1:AvailableInStock ?InStock.
          bind(if(xsd:integer(?InStock) >= xsd:integer(?Quantity),"True", "False") as ?ReadyForTransport).
          bind(if(xsd:integer(?InStock) >= xsd:integer(?Quantity),"0", xsd:integer(?Quantity) - xsd:integer(?InStock)) as ?ProductsToProduce).
          ?Product ns1:ProductionProcess ?Process.
          ?Process ns1:ProductionLine ?ProductionLine.
          ?ProductionLine ns1:ProductionTimePerItem ?TimePerItem.
          ?ProductionLine ns1:Machines ?Ms.
          ?Ms ns1:FreeIn ?MachineFreeIn.
          bind(if(xsd:integer(?ProductsToProduce) = 0, "",  xsd:integer(?TimePerItem) * xsd:integer(?ProductsToProduce)) as ?ProductionTime).
          bind(if(xsd:integer(?ProductsToProduce) = 0, "",  xsd:integer(?ProductionTime) + xsd:integer(?MachineFreeIn)) as ?NewProductsReadyIn).
          
       }
       ORDER BY DESC(xsd:integer(?MachineFreeIn)) LIMIT 1
       """)
       

for row in qres3:
    print("%s  %s    %s     %s          %s                  %s              %s                  %s                %s" % row)
