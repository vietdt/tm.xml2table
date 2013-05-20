<?xml version="1.0" encoding="iso-8859-1"?>
<!--Property of Wayne Glover wglover@docentims.com-->
<!--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <!--start of page.-->
    <div class="content">
      <h1 class="documentFirstHeading"><xsl:value-of select="theMeadows/inspYr"/> Initial Weedwalk Results</h1>
      <div class="documentDescription">There were <span id="count_div1">xx</span>homes in Division 1 and <span id="count_div2">xx</span>homes in Division 2 that failed in initial weedwalk.</div>
      <div class="tabs_container"  style="width:96%">
        <ul id="toc">
          <li class="current" id="ttab5" onclick="tab('tab5')"> <a href="javascript::tab('tab5')" onClick="javascript:tab('tab5')">Division 1</a> </li>
          <li id="ttab6" onclick="tab('tab6')"> <a href="javascript::tab('tab6')" onClick="javascript:tab('tab6')">Division 2</a> </li>
        </ul>
        <div class="content" id="tab5" style="width:100%;padding:0px;">
          <table class="listing" style="width:100%">
            <tr bgcolor="#9acd32">
              <th>Div</th>
              <th>Lot</th>
              <th>Number</th>
              <th>Street</th>
              <th>Result</th>
              <th>Required</th>
              <th>Recommended</th>
              <th>General Comments</th>
              <th>Team Member</th>
            </tr>
            <xsl:for-each select="//theMeadows/home">
              <xsl:if test="homeDiv = 01">
                <tr>
                  <td><xsl:value-of select="homeDiv" /></td>
                  <td><xsl:value-of select="homeLot" /></td>
                  <td><xsl:value-of select="homeAdrNumb" /></td>
                  <td width="140"><xsl:value-of select="homeAdrStreet" /></td>
                  <td><xsl:value-of select="currentYrRslt" /></td>
                  <td width="200"><xsl:value-of select="requirements/requirement" /></td>
                  <td width="200"><xsl:value-of select="recommendations/recommendation" /></td>
                  <td><xsl:value-of select="findingsGeneralComment" /></td>
                  <td width="30"><xsl:value-of select="teamMemberName" /></td>
                </tr>
              </xsl:if>
            </xsl:for-each>
          </table>
          <div style="float:left;width:100%;">
            <hr style="color:#9acd32;background-color:#9acd32;height:.1em;" />
            <div class="bottomtexthere">These homes will be re-inspected during rewalk</div>
          </div>
        </div>
        <div class="content" id="tab6" style="display:none;width:100%;padding:0px;">
          <table class="listing" style="width:100%">
            <tr bgcolor="#9acd32">
              <th>Div</th>
              <th>Lot</th>
              <th>Number</th>
              <th>Street</th>
              <th>Result</th>
              <th>Required</th>
              <th>Recommended</th>
              <th>General Comments</th>
              <th>Team Member</th>
            </tr>
            <xsl:for-each select="theMeadows/home">
              <xsl:if test="homeDiv = 02">
                <tr>
                  <td><xsl:value-of select="homeDiv" /></td>
                  <td><xsl:value-of select="homeLot" /></td>
                  <td><xsl:value-of select="homeAdrNumb" /></td>
                  <td  width="140"><xsl:value-of select="homeAdrStreet" /></td>
                  <td><xsl:value-of select="currentYrRslt" /></td>
                  <td width="200"><xsl:value-of select="requirements/requirement" /></td>
                  <td width="200"><xsl:value-of select="recommendations/recommendation" /></td>
                  <td><xsl:value-of select="findingsGeneralComment" /></td>
                  <td width="30"><xsl:value-of select="teamMemberName" /></td>
                </tr>
              </xsl:if>
            </xsl:for-each>
          </table>
          <div style="float:left;width:100%;">
            <hr style="color:#9acd32;background-color:#9acd32;height:.1em;" />
            <div class="bottomtexthere">These homes will be re-inspected during rewalk</div>
          </div>
        </div>
      </div>
    </div>
  </xsl:template>
</xsl:stylesheet>